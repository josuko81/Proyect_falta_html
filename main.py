from fastapi import Depends, FastAPI, Body, HTTPException, Path, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session, engine, Base
from models.lista import lista as listaModel
from dictionary import list_nutrition

app = FastAPI()
app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"
nutrition = list_nutrition

Base.metadata.create_all(bind=engine)

class otro_nombre(BaseModel):
    id: Optional[int] = None
    Country: str
    State_lgd_code: int
    State: str
    Yearcode: int
    Year: str
    From_year: int
    Residence: str
    Stunted_children_under_5_percent: float
    Severely_stunted_children_under_5_percent: float
    Wasted_children_under_5_percent: float
    Severely_wasted_children_under_5_percent: float
    Underweight_children_under_5_percent: float
    Severely_underweight_children_under_5_percent: float
    Children_6_59_months_muac_lt_12_5_percent: float
    Children_6_59_months_muac_lt_11_5_percent: float
    Children_6_59_months_muac_lt_minus_2_sd_percent: float
    Children_6_59_months_muac_lt_minus_3_sd_percent: float
    Children_under_5_triceps_skinfold_lt_minus_2_sd_percent: float
    Children_under_5_triceps_skinfold_lt_minus_3_sd_percent: float
    Children_under_5_triceps_skinfold_gt_plus_2_sd_percent: float
    Children_under_5_triceps_skinfold_gt_plus_3_sd_percent: float
    Children_1_4_years_subscapular_skinfold_lt_minus_2_sd_percent: float
    Children_1_4_years_subscapular_skinfold_lt_minus_3_sd_percent: float
    Children_1_4_years_subscapular_skinfold_gt_plus_2_sd_percent: float
    Children_1_4_years_subscapular_skinfold_gt_plus_3_sd_percent: float
    Stunted_children_5_9_years_percent: float
    Severely_stunted_children_5_9_years_percent: float
    Moderate_severely_thin_children_5_9_years_lt_minus_2_sd_percent: float
    Severely_thin_children_5_9_years_lt_minus_3_sd_percent: float
    Overweight_obese_children_5_9_years_gt_plus_1_sd_percent: float
    Overweight_obese_children_5_9_years_gt_plus_2_sd_percent: float
    Moderate_severely_thin_adolescents_10_14_years_lt_minus_2_sd_percent: float
    Moderate_severely_thin_adolescents_15_19_years_lt_minus_2_sd_percent: float
    Moderate_severely_thin_adolescents_10_19_years_lt_minus_2_sd_percent: float
    Severely_thin_adolescents_10_14_years_lt_minus_3_sd_percent: float
    Severely_thin_adolescents_15_19_years_lt_minus_3_sd_percent: float
    Severely_thin_adolescents_10_19_years_lt_minus_3_sd_percent: float
    Overweight_obese_adolescents_10_14_years_gt_plus_1_sd_percent: float
    Overweight_obese_adolescents_15_19_years_gt_plus_1_sd_percent: float
    Overweight_obese_adolescents_10_19_years_gt_plus_1_sd_percent: float
    Obese_adolescents_10_14_years_gt_plus_2_sd_percent: float
    Obese_adolescents_15_19_years_gt_plus_2_sd_percent: float
    Obese_adolescents_10_19_years_gt_plus_2_sd_percent: float

@app.get('/', tags=["home"])
def message():
    return HTMLResponse("<h1>Hello world<h1>")

@app.get("/nutrition", tags=["nutrition"], response_model=otro_nombre, status_code=200)
def get_list():
    return JSONResponse(content=nutrition)

@app.get("/nutrition/{id}", tags=["id_nutrition"], response_model=otro_nombre)
def get_nutrition(id: int) -> otro_nombre:
    for item in nutrition:
        if item["id"] == id:
            return JSONResponse(content=item)
    return JSONResponse(status_code=404, content=[])

@app.get("/nutrition/", tags=["id_nutrition"], response_model=List[otro_nombre])
def get_nutrition_by_Residence(Residence: str) -> List[otro_nombre]:
    data = [ item for item in nutrition if item['Residence'] == Residence ]
    return JSONResponse(content=data)

@app.post("/nutrition", tags=["id_nutrition"], response_model=dict, status_code=201)
def create_list(nutrition: otro_nombre) -> dict:
        db = Session()
        new_lista = listaModel(**nutrition.dict())
        db.add(new_lista)
        db.commit()
        db.close()  # Cerrar la sesión después de usarla
        return JSONResponse(status_code=201, content={"message": "Se ha registrado la película"})

@app.put("/nutrition/{id}", tags=["id_nutrition"], response_model=dict, status_code=200)
def update_nutrition(id: int, nutrition:otro_nombre) -> dict:
    for item in nutrition:
        if item["id"] == id:
                item['Country'] = list.Country
                item['State lgd code'] = list.State_lgd_code
                item['State'] = list.State
                item['Yearcode'] = list.Yearcode
                item['Year'] = list.Year
                item['From year'] = list.From_year
                item['Residence type'] = list.Residence
                item['Stunted children under the age of 5 years (%)'] = list.Stunted_children_under_5_percent
                item['Severely stunted children under the age of 5 years (%)'] = list.Severely_stunted_children_under_5_percent
                item['Wasted children under the age of 5 years (%)'] = list.Wasted_children_under_5_percent
                item['Severely wasted children under the age of 5 years (%)'] = list.Severely_wasted_children_under_5_percent
                item['Underweight children under the age of 5 years (%)'] = list.Underweight_children_under_5_percent
                item['Severely underweight children under the age of 5 years (%)'] = list.Severely_underweight_children_under_5_percent
                item['Children age group of 6 to 59 months with mid-upper arm circumference ( muac ) less than 12.5 cm (%)'] = list.Children_6_59_months_muac_lt_12_5_percent
                item['Children age group of 6 to 59 months with mid-upper arm circumference ( muac ) less than 11.5 cm (%)'] = list.Children_6_59_months_muac_lt_11_5_percent
                item['Children age group of 6 to 59 months with mid-upper arm circumference ( muac ) less than -2 sd (%)'] = list.Children_6_59_months_muac_lt_minus_2_sd_percent
                item['Children age group of 6 to 59 months with mid-upper arm circumference ( muac ) less than -3 sd (%)'] = list.Children_6_59_months_muac_lt_minus_3_sd_percent
                item['Children under the age group of 5 years with triceps skinfold (%) less than -2 sd (%)'] = list.Children_under_5_triceps_skinfold_lt_minus_2_sd_percent
                item['Children under the age of 5 years with triceps skinfold less than -3 sd (%)'] = list.Children_under_5_triceps_skinfold_lt_minus_3_sd_percent
                item['Children under the age 5 years with triceps skinfold greater than +2 sd (%)'] = list.Children_under_5_triceps_skinfold_gt_plus_2_sd_percent
                item['Children under the age of 5 years with triceps skinfold greater than +3 sd(%)'] = list.Children_under_5_triceps_skinfold_gt_plus_3_sd_percent
                item['Children age group of 1 to 4 years with subscapular skinfold less than -2 sd (%)'] = list.Children_1_4_years_subscapular_skinfold_lt_minus_2_sd_percent
                item['Children age group of 1 to 4 years with subscapular skinfold less than -3 sd (%)'] = list.Children_1_4_years_subscapular_skinfold_lt_minus_3_sd_percent
                item['Children age group of 1 to 4 years subscapular skinfold greater than +2 sd (%)'] = list.Children_1_4_years_subscapular_skinfold_gt_plus_2_sd_percent
                item['Children age group of 1 to 4 years with subscapular skinfold greater than +3 sd (%)'] = list.Children_1_4_years_subscapular_skinfold_gt_plus_3_sd_percent
                item['Stunted children age group of 5 to 9 years (%)'] = list.Stunted_children_5_9_years_percent
                item['Severely stunted children age group of 5 to 9 years (%)'] = list.Severely_stunted_children_5_9_years_percent
                item['Moderate or severely thin children age group of 5 to 9 years less than -2 sd (%)'] = list.Moderate_severely_thin_children_5_9_years_lt_minus_2_sd_percent
                item['Severely thin children age group of 5 to 9 years less than -3 sd (%)'] = list.Severely_thin_children_5_9_years_lt_minus_3_sd_percent
                item['Overweight or obese children age group of 5-9 years greater than +1 sd (%)'] = list.Overweight_obese_children_5_9_years_gt_plus_1_sd_percent
                item['Overweight or obese children age group of 5-9 years greater than +2 sd (%)'] = list.Overweight_obese_children_5_9_years_gt_plus_2_sd_percent
                item['Moderate or severely thin adolescents age group of 10 to 14 years less than -2 sd (%)'] = list.Moderate_severely_thin_adolescents_10_14_years_lt_minus_2_sd_percent
                item['Moderate or severely thin adolescents age group of 15 to 19 years less than -2 sd (%)'] = list.Moderate_severely_thin_adolescents_15_19_years_lt_minus_2_sd_percent
                item['Moderate or severely thin adolescents age group of 10 to 19 years  less than -2 sd (%)'] = list.Moderate_severely_thin_adolescents_10_19_years_lt_minus_2_sd_percent
                item['Severely thin adolescents age group of 10 to 14 years less than -3 sd (%)'] = list.Severely_thin_adolescents_10_14_years_lt_minus_3_sd_percent
                item['Severely thin adolescents age group of 15 to 19 years less than -3 sd (%)'] = list.Severely_thin_adolescents_15_19_years_lt_minus_3_sd_percent
                item['Severely thin adolescents age group of 10 to 19 years less than -3 sd (%)'] = list.Severely_thin_adolescents_10_19_years_lt_minus_3_sd_percent
                item['Overweight or obese adolescents age group of 10 to 14 years greater than +1 sd (%)'] = list.Overweight_obese_adolescents_10_14_years_gt_plus_1_sd_percent
                item['Overweight or obese adolescents age group of 15 to 19 years greater than +1 sd (%)'] = list.Overweight_obese_adolescents_15_19_years_gt_plus_1_sd_percent
                item['Overweight or obese adolescents age group of 10 to 19 years greater than +1 sd (%)'] = list.Overweight_obese_adolescents_10_19_years_gt_plus_1_sd_percent
                item['Obese adolescents age group of 10 to 14 years greater than +2 sd (%)'] = list.Obese_adolescents_10_14_years_gt_plus_2_sd_percent
                item['Obese adolescents age group of 15 to 19 years greater than +2 sd (%)'] = list.Obese_adolescents_15_19_years_gt_plus_2_sd_percent
                item['Obese adolescents age group of 10 to 19 years greater than +2 sd (%)'] = list.Obese_adolescents_10_19_years_gt_plus_2_sd_percent
                return JSONResponse(content={"message": "Se ha modificado la película"})
                        
@app.delete("/nutrition/{id}", tags=["id_nutrition"], response_model=dict, status_code=200)            
def delete_nutrition(id: int) -> dict:
    for item in nutrition:
        if item["id"] == id:
            nutrition.remove(item)
            return JSONResponse(content={"message": "Se ha eliminado la película"})
