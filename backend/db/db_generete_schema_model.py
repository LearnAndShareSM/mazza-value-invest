import pandas as pd
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date


def generate_and_save_sqlalchemy_model(df, class_name, filename, primary_keys=[]):
    Base = declarative_base()

    attrs = {"__tablename__": class_name.lower()}

    code_lines = [f"class {class_name}(Base):"]
    code_lines.append(f"    __tablename__ = '{class_name.lower()}'")

    for col, dtype in df.dtypes.items():
        if "int" in str(dtype):
            column_type = "Integer"
        elif "float" in str(dtype):
            column_type = "Float"
        elif "datetime" in str(dtype):
            column_type = "Date"
        else:
            column_type = "String"

        if col in primary_keys:
            attrs[col] = Column(eval(column_type), primary_key=True)
            code_lines.append(f"    {col} = Column({column_type}, primary_key=True)")
        else:
            attrs[col] = Column(eval(column_type))
            code_lines.append(f"    {col} = Column({column_type})")

    type(class_name, (Base,), attrs)

    model_code = "\n".join(code_lines)

    with open(filename, "w") as f:
        imports = """\
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date
Base = declarative_base()
"""
        f.write(imports)
        f.write("\n")
        f.write(model_code)

    return model_code


# Esempio di utilizzo:
# Assumendo che tu possa caricare df_final da qualche parte, ad esempio:
# df_final = pd.read_csv('path_to_your_dataframe.csv')

# generate_and_save_sqlalchemy_model(df_final, "Balance", "generated_balance_model.py", ['cik', 'ticker', 'accepted_date', 'filling_date', 'calendar_year', 'period'])
