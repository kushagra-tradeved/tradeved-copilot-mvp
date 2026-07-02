import pandas as pd

def load_state_mapping(longform_path, transition_path):
    df_lf = pd.read_excel(longform_path, sheet_name='LongForm_200')
    df_st = pd.read_excel(transition_path, sheet_name='State_Transition_60')
    
    # Strip whitespace from column headers
    df_lf.columns = df_lf.columns.str.strip()
    df_st.columns = df_st.columns.str.strip()
    
    mapping = df_st[['start_state', 'mentor_primary_task', 'mentor_failure_risk']].drop_duplicates(subset=['start_state'])
    return pd.merge(df_lf, mapping, left_on='mentee_start_state', right_on='start_state', how='left')