BASE_URL = "https://smartup.online/b"

USERNAME = "tjasur@test"
PASSWORD = "01062001"

HEADERS = {
    "project_code": "trade",
    "filial_id": "7097033",
    "Content-Type": "application/json"
}

# API endpointlar
ENDPOINTS = {
    "purchase_import": f"{BASE_URL}/anor/mxsx/mkw/purchase$import",
    "purchase_export": f"{BASE_URL}/anor/mxsx/mkw/purchase$export",
    "input_import": f"{BASE_URL}/anor/mxsx/mkw/input$import",
    "input_export": f"{BASE_URL}/anor/mxsx/mkw/input$export",
}
