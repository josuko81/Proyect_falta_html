from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class lista(Base):
    
    __tablename__ = "nutrition_data"
    
    id = Column(Integer, primary_key= True)
    Country = Column(String)
    State_lgd_code = Column(Integer)
    State = Column(String)
    Yearcode = Column(Integer)
    Year = Column(String)
    From_year = Column(Integer)
    Residence = Column(String)
    Stunted_children_under_5_percent = Column(Float)
    Severely_stunted_children_under_5_percent = Column(Float)
    Wasted_children_under_5_percent = Column(Float)
    Severely_wasted_children_under_5_percent = Column(Float)
    Underweight_children_under_5_percent = Column(Float)
    Severely_underweight_children_under_5_percent = Column(Float)
    Children_6_59_months_muac_lt_12_5_percent = Column(Float)
    Children_6_59_months_muac_lt_11_5_percent = Column(Float)
    Children_6_59_months_muac_lt_minus_2_sd_percent = Column(Float)
    Children_6_59_months_muac_lt_minus_3_sd_percent = Column(Float)
    Children_under_5_triceps_skinfold_lt_minus_2_sd_percent = Column(Float)
    Children_under_5_triceps_skinfold_lt_minus_3_sd_percent = Column(Float)
    Children_under_5_triceps_skinfold_gt_plus_2_sd_percent = Column(Float)
    Children_under_5_triceps_skinfold_gt_plus_3_sd_percent = Column(Float)
    Children_1_4_years_subscapular_skinfold_lt_minus_2_sd_percent = Column(Float)
    Children_1_4_years_subscapular_skinfold_lt_minus_3_sd_percent = Column(Float)
    Children_1_4_years_subscapular_skinfold_gt_plus_2_sd_percent = Column(Float)
    Children_1_4_years_subscapular_skinfold_gt_plus_3_sd_percent = Column(Float)
    Stunted_children_5_9_years_percent = Column(Float)
    Severely_stunted_children_5_9_years_percent = Column(Float)
    Moderate_severely_thin_children_5_9_years_lt_minus_2_sd_percent = Column(Float)
    Severely_thin_children_5_9_years_lt_minus_3_sd_percent = Column(Float)
    Overweight_obese_children_5_9_years_gt_plus_1_sd_percent = Column(Float)
    Overweight_obese_children_5_9_years_gt_plus_2_sd_percent = Column(Float)
    Moderate_severely_thin_adolescents_10_14_years_lt_minus_2_sd_percent = Column(Float)
    Moderate_severely_thin_adolescents_15_19_years_lt_minus_2_sd_percent = Column(Float)
    Moderate_severely_thin_adolescents_10_19_years_lt_minus_2_sd_percent = Column(Float)
    Severely_thin_adolescents_10_14_years_lt_minus_3_sd_percent = Column(Float)
    Severely_thin_adolescents_15_19_years_lt_minus_3_sd_percent = Column(Float)
    Severely_thin_adolescents_10_19_years_lt_minus_3_sd_percent = Column(Float)
    Overweight_obese_adolescents_10_14_years_gt_plus_1_sd_percent = Column(Float)
    Overweight_obese_adolescents_15_19_years_gt_plus_1_sd_percent = Column(Float)
    Overweight_obese_adolescents_10_19_years_gt_plus_1_sd_percent = Column(Float)
    Obese_adolescents_10_14_years_gt_plus_2_sd_percent = Column(Float)
    Obese_adolescents_15_19_years_gt_plus_2_sd_percent = Column(Float)
    Obese_adolescents_10_19_years_gt_plus_2_sd_percent = Column(Float)