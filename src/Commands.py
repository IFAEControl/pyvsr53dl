"""
Thyracont Communication Protocol Command Listing
"""

class Commands():
    # Available Commands for VSR53DL
    Type_Device = 'TD'
    Product_Name = 'PN'
    Serial_Number_Device = 'SD'
    Serial_Number_Head = 'SH'
    Baud_Rate = 'BR'
    Response_Delay = 'RD'
    Version_Device = 'VD'
    Version_Firmware = 'VF'
    Version_Bootloader = 'VB'
    Device_Restart = 'DR'

    Measurement_Range = 'MR'
    Measurement_Value = 'MV'
    Measurement_Value_1 = 'M1' # (Pirani)
    Measurement_Value_2 = 'M2'  # (Piezo)
    Display_Unit = 'DU'
    Display_Orientation = 'DO'
    Relay_1 = 'R1'
    Relay_2 = 'R2'
    Adjust_High = 'AH'
    Adjust_Low = 'AL'

    Sensor_Transition = 'ST'
    Gas_Correction_Factor_1 = 'C1' # (Pirani)
    Analog_Output_Characteristic = 'OC'
    Operating_Hours = 'OH'


    # Rest of Commands available in the protocol
    Measurement_Value_3_HOT_C = 'M3'
    Measurement_Value_4_COLD_C = 'M4'
    Measurement_Value_6_AMB_P = 'M6'
    Measurement_Value_7_REL_P = 'M7'
    Relay_3 = 'R3'
    Relay_4 = 'R4'

    Display_Data_Source = 'DD'

    Degas = 'DG'
    Digital_Logic = 'DL'

    Cathode_Control = 'CC'
    Cathode_Control_Mode = 'CM'
    Filament_Control = 'FC'
    Filament_Number = 'FN'
    FilamentStatus = 'FS'

    Gas_Correction_Factor_3 = 'C3' #  (Hot Cathode)
    Gas_Correction_Factor_4 = 'C4' #  (Cold Cathode)

    Panel_Status = 'PS'
    Controller_Status = 'CS'
