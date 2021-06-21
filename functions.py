def edu_func(df):
        df['Dem_edu'] = df['Dem_edu'].replace({'Uninformative response': 0, 'None': 1, 'Up to 6 years of school': 2, 'Up to 9 years of school': 3,
                                            'Up to 12 years of school': 4, 'Some College, short continuing education or equivalent': 5, 'College degree, bachelor, master': 6, 'PhD/Doctorate': 7})
        return df[['Dem_edu']]

def edu_mom_func(df):
    df['Dem_edu_mom'] = df['Dem_edu_mom'].replace({'Uninformative response': 0, 'None': 1, 'Up to 6 years of school': 2, 'Up to 9 years of school': 3,
                                                'Up to 12 years of school': 4, 'Some College or equivalent': 5, 'College degree': 6, 'PhD/Doctorate': 7})
    return df[['Dem_edu_mom']]

def edu_risk_group(df):
    df['Dem_riskgroup'] = df['Dem_riskgroup'].replace(
        {'No': 1, 'Not sure': 2, 'Yes': 3})
    return df[['Dem_riskgroup']]

def dem_expat_func(df):
    df['Dem_Expat'] = df['Dem_Expat'].replace({'no': 0, 'yes': 1})
    return df[['Dem_Expat']]