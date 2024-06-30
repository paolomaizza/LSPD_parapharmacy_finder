from datetime import datetime
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from .mymodules.parapharmacies import (
    find_by_region,
    is_valid_region,
    list_regions,
    list_provinces,
    list_cities,
    find_by_region_province_and_city
)
from .product import get_product_details
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Enable CORS to allow cross-origin requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Root endpoint returning a simple JSON response
@app.get('/')
def read_root():
    return {"Hello": "World"}

# Endpoint to query parapharmacies by region code
@app.get('/query/{region}')
def read_item(region: str):
    try:
        region = int(region)  # Convert region to integer
    except ValueError:
        return {"error": "Invalid format. Expecting a numeric region code"}
    if is_valid_region(region):  # Check if region code is valid
        return {"region": region, "parapharmacies": find_by_region(region)}
    else:
        return {"error": f"Invalid region code {region}"}

# Endpoint to get the current date and time in ISO format
@app.get('/get-date')
def get_date():
    current_date = datetime.now().isoformat()
    return JSONResponse(content={"date": current_date})

# Endpoint to list all available regions
@app.get('/regions')
def get_regions():
    return {"regions": list_regions()}

# Endpoint to list provinces in a specific region
@app.get('/regions/{region_code}/provinces')
def get_provinces(region_code: int):
    return {"provinces": list_provinces(region_code)}

# Endpoint to list cities in a specific province within a region
@app.get('/regions/{region_code}/provinces/{province_name}/cities')
def get_cities(region_code: int, province_name: str):
    return {"cities": list_cities(region_code, province_name)}

# Endpoint to list pharmacies in a specific city, province, and region
@app.get(
    '/regions/{region_code}/provinces/{province_name}/cities/{city_name}/'
    'pharmacies'
)
def get_pharmacies(region_code: int, province_name: str, city_name: str):
    return {
        "pharmacies": find_by_region_province_and_city(
            region_code, province_name, city_name
        )
    }

# Endpoint to search for product details by product name
@app.get('/search-product')
def search_product(
    product_name: str = Query(
        ..., description="Name of the product to search"
    )
):
    product_details = get_product_details()
    product_name = product_name.strip().upper()  # Normalize product name
    if product_name in product_details:
        return {
            "product": product_name,
            "details": product_details[product_name]
        }
    else:
        raise HTTPException(
            status_code=404,
            detail=(
                f"The product '{product_name}' is not available "
                "in the pharmacy."
            )
        )

