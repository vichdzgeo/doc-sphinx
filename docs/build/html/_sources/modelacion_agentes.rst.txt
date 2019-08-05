Modelación basada en agentes
##############################

Insumos
********

Modelos multicriterio
======================

Residentes
-----------

:download:`Iztapalapa <../modelos_mcda/I080316_OTR.sdmod>`.

Sistema de Aguas de la Ciudad de México (SACMEX)
--------------------------------------------------

:download:`SACMEX <../modelos_mcda/Modelo_sacmex_sesmo.sdmod>`.


Variables geográficas del modelo:
==================================

===========================================================   ===========================================================================================================
Variables                                                     Descripción
===========================================================   ===========================================================================================================
resident_potable_water_lacking_count                          Represent the population of each census block that does not have access to piped water in their houses
censusblock_id                                                An universal identifier of each census block that includes the municipality, and the state.
infrastructure_age                                            Proxy for the age of infrastructure based on the sequence of urbanization periods in CDMX
area
garbage_index                                                 Proxy of the amount of garbage produced in each census block
sewer_system_pump_count                                       Number of pumps to direct stormwater in the sewer system
waterquality_index                                            Reports about the quality of the water per census block
urbangrowth                                                   Proportion of urbanized area in a census block
criticalzone                                                  Areas of the city SACMEX considers critical because of the difficulties of providing potable water
geographic_id
resident_potable_water_waste_perception                       Perception of residents about exportation potable water
resident_potable_water_export_perception                      Perception of residents about net potable water exports
resident_diarrhea_per_capita                                  Number of cases of Diarrheal diseases per 10000 individual in the year 2014
resident_reports_potable_water_failure_count_per_year         Number of reports of failures in the distribution potable water
resident_reports_sewer_failure_count_per_year                 Number of reports collected by sacmex about failure in the sewer system
household_potable_system_lacking_percent                      Proportion of households without connection to potable water distribution infrastructure
household_sewer_system_lacking_percent                        Proportion of households without connection to the sewer system
resident_income_per_capita                                    Income per capita in dollars (by municipality)
resident_asset_index                                          Resident asset index (by census block)
resident_reports_flooding_per_year                            Frequency of flooding event in a year
household_days_no_potable_water_per_week_mean                 Average number of days in a week a census block is without water. Data from INEGI
sewer_system_segment_count                                    Number of segments of the sewer system in each census block
delegation_social_pressure                                    Proxy for the attention government give to different delegations
resident_count                                                Total population per census block
potable_system_pressure
media_social_pressure                                         Proxy for media report about water scarcity or flooding events
resident_reports_ponding_per_year
sewer_system_capacity_max                                     Total population per census block
sewer_system_storm_drain_count                                Number of drainage per census block
runoff_presence
subsidence_rate_per_year  	                                  Rate of subsidence per year
household_water_storage_tank_available_percent                Proportion of houses with water storage tanks
resident_reports_potable_water_failure_count_per_area_year
===========================================================   ===========================================================================================================





Issues
*******

Códigos
*******


Salidas
********
