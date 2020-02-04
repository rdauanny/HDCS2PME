import pandas as pd
import sqlalchemy as sql

def sql_connect(server_pme):
    import sqlalchemy as sql
    server_pme = 'vwin12r0000'
    server_ope = ''

    ion_data = sql.create_engine('mssql+pyodbc://' + server_pme +'\ION/ION_Data?driver=SQL+Server+Native+Client+11.0')
    ion_network = sql.create_engine('mssql+pyodbc://localhost\ION/ION_Network?driver=SQL+Server+Native+Client+11.0')
    ion_systemlog = sql.create_engine('mssql+pyodbc://localhost\ION/ION_SystemLog?driver=SQL+Server+Native+Client+11.0')
    sys = sql.create_engine('mssql+pyodbc://localhost\ION/master?driver=SQL+Server+Native+Client+11.0')

    sql = ''' Select * FROM sys.fn_dblog(NULL,NULL) '''
    log = pd.read_sql_query(sql, ion_network)
    log = log[log.Operation == "LOP_INSERT_ROWS"]

    #Name, Display Name
    Source = pd.read_sql_table('SRC_Source', ion_network)
    Devices = pd.read_sql_table('Device', ion_network)

def csv_export(filename):

    devicestemplates = ['$PM82xxEMGP','$PM53xxEMGP', '$PM5350MBGP','$ATV9xxEGP', '$ATV6xxEGP', '$TesysTEGP',
                 '$ATS22MBGP', '$ATS48MBGP', '$Sepam80MBGP', '$CompactNSXMBUGP',
                 '$MasterpactMTZMBUGP', '$MasterpactNxCMBUGP', '$MasterpactNxMBUGP',
                 '$CompactHWGP', '$MasterpactHWGP']

    csv = pd.read_csv(filename, header=1)
    csv = csv.loc[:,['$Location', '$InstanceName','$InstanceTemplateIdentifier']].drop_duplicates()
    csv = csv[csv['$InstanceTemplateIdentifier'].isin(devicestemplates)].reset_index(drop= True)
    return csv





