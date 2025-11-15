string button.placeDandHLicenseOrder1(String invoiceId)
{
try 
{
	// ===========
	// CONFIGURATION
	// ===========
	STATUS_NOT_ORDERED = "Not Ordered";
	STATUS_PROCESSING = "Processing";
	STATUS_SUCCESS = "Success";
	STATUS_FAILED = "Failed";
	FIELD_STATUS = "D_H_Order_Status";
	FIELD_ERRMSG = "D_H_Error_Message";
	FIELD_CONFIRM = "D_H_Confirmation_Number";
	DANDH_VENDOR_ID = "835703000135684001";
	LICENSE_KEYWORD = "Chrome Enterprise Upgrade EDU";
	CSV_BACKEND_URL = "http://smtp.macservice.com:3000/create-and-send-csv";
	// --- D&H API CONFIG ---
	// 	DH_AUTH_URL = "https://auth.dandh.com/api/oauth/token";
	// If your org uses the v2 path keep as-is; otherwise use: https://api.dandh.com/customers
	// 	DH_API_BASE = "https://api.dandh.com/customerOrderManagement/v2/customers";
	// 	DH_AUTH_URL = "https://auth.dandh.com/api/oauth/token";
	DH_AUTH_URL = "https://test.auth.dandh.com/api/oauth/token";
	DH_API_BASE = "https://test.api.dandh.com/customerOrderManagement/v2/customers";
	// 	DH_CLIENT_ID = "eadb71b4-e3af-4b15-b036-fedbf580591f";
	// 	DH_CLIENT_SECRET = "e204edfb-4e71-4aba-baa0-72827bac970e";
	DH_CLIENT_ID = "855691ab-3456-4e4c-ba8b-03ec5e5f5400";
	DH_CLIENT_SECRET = "561dd443-6e1c-444f-a89c-6f2104eadf5a";
	DH_TENANT = "dhus";
	DH_ACCOUNT_NUMBER = "3014500000";
	// ===========
	// START EXECUTION
	// ===========
	if(invoiceId == null || invoiceId.trim().isEmpty())
	{
		return "❌ Missing invoiceId.";
	}
	invIdLong = invoiceId.toLong();
	// 1) Fetch Invoice
	invoice = zoho.crm.getRecordById("Invoices",invIdLong);
	if(invoice == null || invoice.isEmpty())
	{
		return "❌ Invoice not found.";
	}
	info "Invoice: " + invoice;
	// 2) Prevent duplicate orders
	currentStatus = ifnull(invoice.get(FIELD_STATUS),"");
	if(currentStatus != "" && !currentStatus.equalsIgnoreCase(STATUS_NOT_ORDERED))
	{
		return "⚠️ Already processed. Status: " + currentStatus;
	}
	// Lock invoice as Processing
	lockMap = Map();
	lockMap.put(FIELD_STATUS,STATUS_PROCESSING);
	zoho.crm.updateRecord("Invoices",invIdLong,lockMap);
	// 3) Gather account and product data
	accountLookup = invoice.get("Account_Name");
	if(accountLookup == null || accountLookup.get("id") == null)
	{
		failMap = Map();
		failMap.put(FIELD_STATUS,STATUS_FAILED);
		failMap.put(FIELD_ERRMSG,"Missing Account on invoice.");
		zoho.crm.updateRecord("Invoices",invIdLong,failMap);
		return "❌ Missing Account.";
	}
	accountId = accountLookup.get("id");
	account = zoho.crm.getRecordById("Accounts",accountId);
	if(account == null)
	{
		failMap = Map();
		failMap.put(FIELD_STATUS,STATUS_FAILED);
		failMap.put(FIELD_ERRMSG,"Account not found.");
		zoho.crm.updateRecord("Invoices",invIdLong,failMap);
		return "❌ Account not found.";
	}
	// Find Chrome license item (by name or Product_Code)
	productDetails = ifnull(invoice.get("Product_Details"),List());
	info "Product_Details: " + productDetails;
	if(productDetails.isEmpty())
	{
		failMap = Map();
		failMap.put(FIELD_STATUS,STATUS_FAILED);
		failMap.put(FIELD_ERRMSG,"No line items on invoice.");
		zoho.crm.updateRecord("Invoices",invIdLong,failMap);
		return "❌ No line items on invoice.";
	}
	licenseQty = 0;
	licenseProductId = "";
	licenseProductName = "";
	licenseProductCodeReadable = "";
	invLinePrice = 0.0;
	kw = LICENSE_KEYWORD.toLowerCase();
	for each  line in productDetails
	{
		productRef = ifnull(line.get("product"),Map());
		nameVal = ifnull(productRef.get("name"),"");
		codeVal = ifnull(productRef.get("Product_Code"),"");
		if(nameVal.toLowerCase().contains(kw) || codeVal.toLowerCase().contains(kw))
		{
			licenseQty = ifnull(line.get("quantity"),0);
			licenseProductId = ifnull(productRef.get("id"),"");
			licenseProductName = nameVal;
			licenseProductCodeReadable = codeVal;
			invLinePrice = ifnull(line.get("list_price"),0.0);
			break;
		}
	}
	if(licenseQty <= 0 || licenseProductId == "")
	{
		failMap = Map();
		failMap.put(FIELD_STATUS,STATUS_FAILED);
		failMap.put(FIELD_ERRMSG,"No Chrome license found.");
		zoho.crm.updateRecord("Invoices",invIdLong,failMap);
		return "❌ No Chrome License found on this invoice.";
	}
	// Fetch full Product to read D&H SKU (alphanumeric)
	prodFull = zoho.crm.getRecordById("Products",licenseProductId);
	info "Product (full): " + prodFull;
	dhSku = ifnull(prodFull.get("D_H_SKU"),"");
	// e.g., CROSSWDISEDUNEW
	if(dhSku == "" || !dhSku.matches("^[A-Za-z0-9]+$"))
	{
		failMap = Map();
		failMap.put(FIELD_STATUS,STATUS_FAILED);
		failMap.put(FIELD_ERRMSG,"Missing/invalid D&H SKU (D_H_SKU) on Product.");
		zoho.crm.updateRecord("Invoices",invIdLong,failMap);
		return "❌ Missing/invalid D&H SKU on Product.";
	}
	// 4) Create Purchase Order in Zoho (reference product by id)
	poMap = Map();
	mtsQuoteNumber = ifnull(invoice.get("MTS_Quote_Number"),"");
	if(mtsQuoteNumber != "")
	{
		poMap.put("PO_Number","License - " + mtsQuoteNumber);
	}
	else
	{
		// Fallback if MTS Quote Number is not available
		poMap.put("PO_Number","License - INV" + invIdLong);
	}

	poMap.put("Subject","Google Licenses for " + ifnull(account.get("Account_Name"),"Customer"));
	vendorRef = Map();
	vendorRef.put("id",DANDH_VENDOR_ID);
	poMap.put("Vendor_Name",vendorRef);
	poProducts = List();
	poItem = Map();
	prodRefMap = Map();
	prodRefMap.put("id",licenseProductId);
	poItem.put("product",prodRefMap);
	poItem.put("quantity",licenseQty);
	if(invLinePrice == null || invLinePrice <= 0)
	{
		invLinePrice = ifnull(prodFull.get("Unit_Price"),1.0);
	}
	poItem.put("list_price",invLinePrice);
	poProducts.add(poItem);
	poMap.put("Product_Details",poProducts);
	poResp = zoho.crm.createRecord("Purchase_Orders",poMap);
	poId = ifnull(poResp.get("id"),"");
	poNumber = ifnull(poResp.get("PO_Number"),"");
	if(poId == "")
	{
		failMap = Map();
		failMap.put(FIELD_STATUS,STATUS_FAILED);
		failMap.put(FIELD_ERRMSG,"Failed to create Purchase Order: " + poResp.toString());
		zoho.crm.updateRecord("Invoices",invIdLong,failMap);
		return "❌ Failed to create Purchase Order.";
	}
	// 5) OAuth (defensive toMap)
	authResponse = invokeurl
	[
		url :DH_AUTH_URL
		type :POST
		parameters:{"grant_type":"client_credentials","client_id":DH_CLIENT_ID,"client_secret":DH_CLIENT_SECRET,"scope":"resource.WRITE resource.READ resource.ADMIN"}
		headers:{"Content-Type":"application/x-www-form-urlencoded"}
	];
	m = Map();
	try 
	{
		m = authResponse.toMap();
	}
	catch (ex)
	{
		failMap = Map();
		failMap.put(FIELD_STATUS,STATUS_FAILED);
		failMap.put(FIELD_ERRMSG,"OAuth non-JSON response: " + authResponse.toString());
		zoho.crm.updateRecord("Invoices",invIdLong,failMap);
		return "❌ Auth error (non-JSON).";
	}
	accessToken = ifnull(m.get("access_token"),null);
	if(accessToken == null)
	{
		failMap = Map();
		failMap.put(FIELD_STATUS,STATUS_FAILED);
		failMap.put(FIELD_ERRMSG,"Auth Error: " + m.toString());
		zoho.crm.updateRecord("Invoices",invIdLong,failMap);
		return "❌ Failed to authenticate with D&H.";
	}
	mtsQuoteNumber = ifnull(invoice.get("MTS_Quote_Number"),"");
	if(mtsQuoteNumber != "")
	{
		finalCpo = "MTS-" + mtsQuoteNumber + "-LIC";
	}
	else
	{
		invIdStr = invoice.get("id").toString();
		timestamp = zoho.currenttime.getTime().toString();
		finalCpo = "INV-" + invIdStr + "-" + timestamp.substring(timestamp.length() - 6);
	}
	// ---------- Attempt #1 ----------
	orderBody = Map();
	orderBody.put("customerPurchaseOrder",finalCpo);
	deliveryAddress = Map();
	accName = ifnull(account.get("Account_Name"),"Customer");
	deliveryAddress.put("deliveryName",accName);
	addressMap = Map();
	addressMap.put("street",ifnull(invoice.get("Billing_Street"),""));
	addressMap.put("city",ifnull(invoice.get("Billing_City"),""));
	addressMap.put("region",ifnull(invoice.get("Billing_State"),""));
	addressMap.put("postalCode",ifnull(invoice.get("Billing_Code"),""));
	addressMap.put("country","US");
	deliveryAddress.put("address",addressMap);
	orderBody.put("deliveryAddress",deliveryAddress);
	shipments = List();
	shipment = Map();
	shipment.put("branch","BR01");
	lines = List();
	lineItem = Map();
	lineItem.put("item",dhSku);
	lineItem.put("unitPrice","0.00");
	lineItem.put("orderQuantity",licenseQty);
	lineItem.put("externalLineNumber",1);
	lines.add(lineItem);
	shipment.put("lines",lines);
	shipments.add(shipment);
	orderBody.put("shipments",shipments);
	orderBody.put("specialInstructions","Chrome OS License Order via Zoho");
	orderUrl = DH_API_BASE + "/" + DH_ACCOUNT_NUMBER + "/salesOrders";
	headers = Map();
	headers.put("Authorization","Bearer " + accessToken);
	headers.put("dandh-tenant",DH_TENANT);
	headers.put("Content-Type","application/json");
	headers.put("Accept","application/json");
	info "Attempt #1 CPO: " + finalCpo;
	info "Order URL: " + orderUrl;
	info "Order Body: " + orderBody;
	orderResponse = invokeurl
	[
		url :orderUrl
		type :POST
		parameters:orderBody.toString()
		headers:headers
	];
	info "D&H Order Response (attempt 1): " + orderResponse;
	confirmationNumber = ifnull(orderResponse.get("salesOrderNumber"),null);
	if(confirmationNumber == null)
	{
		confirmationNumber = ifnull(orderResponse.get("orderNumber"),null);
		if(confirmationNumber == null)
		{
			confirmationNumber = orderResponse.get("id");
		}
	}
	if(confirmationNumber != null)
	{
		finalUpdate = Map();
		finalUpdate.put(FIELD_STATUS,STATUS_SUCCESS);
		finalUpdate.put(FIELD_CONFIRM,confirmationNumber.toString());
		zoho.crm.updateRecord("Invoices",invIdLong,finalUpdate);
		// CSV (separate headers)
		csvData = Map();
		if(mtsQuoteNumber != "")
		{
			csvData.put("po_number","License - " + mtsQuoteNumber);
		}
		else
		{
			csvData.put("po_number",poNumber); // fallback to auto-generated PO number
		}
		csvData.put("invoice_number",ifnull(invoice.get("Invoice_Number"),invoice.get("id")));
		csvData.put("customer_name",accName);
		csvData.put("sku",dhSku);
		csvData.put("quantity",licenseQty);
		csvData.put("confirmation",confirmationNumber);
		csvData.put("customer_purchase_order",finalCpo);
		csvData.put("purchased_at",zoho.currenttime.toString("yyyy-MM-dd'T'HH:mm:ss'Z'"));
		csvHeaders = Map();
		csvHeaders.put("Content-Type","application/json");
		csvResp = invokeurl
		[
			url :CSV_BACKEND_URL
			type :POST
			parameters:csvData.toString()
			headers:csvHeaders
		];
		info "CSV Response: " + csvResp;
		return "✅ Order successful. Confirmation #: " + confirmationNumber + " | CPO: " + finalCpo;
	}
	// If attempt #1 failed, check duplicate-PO
	errName1 = ifnull(orderResponse.get("errorName"),"");
	errMsg1 = ifnull(orderResponse.get("message"),"");
	errName1Lc = errName1.toLowerCase();
	errMsg1Lc = errMsg1.toLowerCase();
	isDuplicate1 = false;
	if(errName1Lc.contains("internal service call error") && errMsg1Lc.contains("duplicate po number"))
	{
		isDuplicate1 = true;
	}
	else if(errMsg1Lc.contains("duplicate po number"))
	{
		isDuplicate1 = true;
	}
	// ---------- Attempt #2 (only if duplicate) ----------
	if(isDuplicate1 == true)
	{
		mtsQuoteNumber = ifnull(invoice.get("MTS_Quote_Number"),"");
		if(mtsQuoteNumber != "")
		{
			finalCpo = "MTS-" + mtsQuoteNumber + "-LIC-RETRY";
		}
		else
		{
			invIdStr = invoice.get("id").toString();
			timestamp = zoho.currenttime.getTime().toString();
			finalCpo = "INV-" + invIdStr + "-RETRY-" + timestamp.substring(timestamp.length() - 6);
		}
		orderBody2 = Map();
		orderBody2.put("customerPurchaseOrder",finalCpo);
		deliveryAddress2 = Map();
		deliveryAddress2.put("deliveryName",accName);
		addressMap2 = Map();
		addressMap2.put("street",ifnull(invoice.get("Billing_Street"),""));
		addressMap2.put("city",ifnull(invoice.get("Billing_City"),""));
		addressMap2.put("region",ifnull(invoice.get("Billing_State"),""));
		addressMap2.put("postalCode",ifnull(invoice.get("Billing_Code"),""));
		addressMap2.put("country","US");
		deliveryAddress2.put("address",addressMap2);
		orderBody2.put("deliveryAddress",deliveryAddress2);
		shipments2 = List();
		shipment2 = Map();
		shipment2.put("branch","BR01");
		lines2 = List();
		lineItem2 = Map();
		lineItem2.put("item",dhSku);
		lineItem2.put("unitPrice","0.00");
		lineItem2.put("orderQuantity",licenseQty);
		lineItem2.put("externalLineNumber",1);
		lines2.add(lineItem2);
		shipment2.put("lines",lines2);
		shipments2.add(shipment2);
		orderBody2.put("shipments",shipments2);
		orderBody2.put("specialInstructions","Chrome OS License Order via Zoho");
		info "Attempt #2 CPO: " + finalCpo;
		info "Order URL: " + orderUrl;
		info "Order Body: " + orderBody2;
		orderResponse2 = invokeurl
		[
			url :orderUrl
			type :POST
			parameters:orderBody2.toString()
			headers:headers
		];
		info "D&H Order Response (attempt 2): " + orderResponse2;
		confirmationNumber2 = ifnull(orderResponse2.get("salesOrderNumber"),null);
		if(confirmationNumber2 == null)
		{
			confirmationNumber2 = ifnull(orderResponse2.get("orderNumber"),null);
			if(confirmationNumber2 == null)
			{
				confirmationNumber2 = orderResponse2.get("id");
			}
		}
		if(confirmationNumber2 != null)
		{
			finalUpdate = Map();
			finalUpdate.put(FIELD_STATUS,STATUS_SUCCESS);
			finalUpdate.put(FIELD_CONFIRM,confirmationNumber2.toString());
			zoho.crm.updateRecord("Invoices",invIdLong,finalUpdate);
			// CSV (separate headers)
			csvData = Map();
			csvData.put("po_number",poNumber);
			csvData.put("invoice_number",ifnull(invoice.get("Invoice_Number"),invoice.get("id")));
			csvData.put("customer_name",accName);
			csvData.put("sku",dhSku);
			csvData.put("quantity",licenseQty);
			csvData.put("confirmation",confirmationNumber2);
			csvData.put("customer_purchase_order",finalCpo);
			csvData.put("purchased_at",zoho.currenttime.toString("yyyy-MM-dd'T'HH:mm:ss'Z'"));
			csvHeaders = Map();
			csvHeaders.put("Content-Type","application/json");
			csvResp = invokeurl
			[
				url :CSV_BACKEND_URL
				type :POST
				parameters:csvData.toString()
				headers:csvHeaders
			];
			info "CSV Response: " + csvResp;
			return "✅ Order successful. Confirmation #: " + confirmationNumber2 + " | CPO: " + finalCpo;
		}
		// attempt #2 failed as well
		finalUpdate = Map();
		finalUpdate.put(FIELD_STATUS,STATUS_FAILED);
		finalUpdate.put(FIELD_ERRMSG,"API Error (attempt 2): " + orderResponse2.toString());
		zoho.crm.updateRecord("Invoices",invIdLong,finalUpdate);
		return "❌ D&H API Error: " + orderResponse2.toString();
	}
	else
	{
		// not a duplicate; return the first error
		finalUpdate = Map();
		finalUpdate.put(FIELD_STATUS,STATUS_FAILED);
		finalUpdate.put(FIELD_ERRMSG,"API Error (attempt 1): " + orderResponse.toString());
		zoho.crm.updateRecord("Invoices",invIdLong,finalUpdate);
		return "❌ D&H API Error: " + orderResponse.toString();
	}
}
catch (e)
{
	err = Map();
	err.put("D_H_Order_Status","Failed");
	err.put("D_H_Error_Message","System Error: " + e.toString());
	try 
	{
		zoho.crm.updateRecord("Invoices",invoiceId.toLong(),err);
	}
	catch (ex)
	{
		info ex;
	}
	return "❌ System Error: " + e.toString();
}
}