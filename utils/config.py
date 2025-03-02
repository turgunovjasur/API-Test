BASE_URL = "https://smartup.online/b/anor/mxsx/mkw"

USERNAME = "tjasur@test"
PASSWORD = "01062001"

HEADERS = {
    "project_code": "trade",
    "filial_id": "7097033",
    "Content-Type": "application/json"
}

# API endpointlar
ENDPOINTS = {
    "purchase_import": f"{BASE_URL}/purchase$import",
    "purchase_export": f"{BASE_URL}/purchase$export",
    "input_import": f"{BASE_URL}/input$import",
    "input_export": f"{BASE_URL}/input$export",
}
