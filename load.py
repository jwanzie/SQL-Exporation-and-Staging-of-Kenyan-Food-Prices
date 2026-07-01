from sqlalchemy import create_engine 



def load_to_mysql(df):
  engine = create_engine('mysql+pymysql://root:Hahaha!1!@localhost:3306/food_prices_ken')

  df.to_sql(
  name = 'staging_food_prices',
  con = engine,
  if_exists = 'append',
  index = False)

  print('Successfully added and loaded to food_prices_ken db')

if __name__ == '__main__':

  from extract import load_data
  from clean import clean_data

  csv_path = '/Users/lilianmaina/Desktop/Projects/DataEngineeringProject/wfp_food_prices_ken.csv'

  df = load_data(csv_path)

  df = clean_data(df)

  load_to_mysql(df)