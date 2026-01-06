import numpy as np
import pandas  as pd
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import OneHotEncoder , StandardScaler
from sklearn.pipeline import  Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from  sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import cross_val_score


housing  = pd.read_csv("_05_Practical_ML_using_Scikitlearn\housing.csv")


housing["income_cat"] = pd.cut(
    housing["median_income"],
    bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
    labels=[1, 2, 3, 4, 5]
)


split = StratifiedShuffleSplit(n_splits=1 , test_size=0.2, random_state=42)

for train_index , test_index in split.split(housing, housing["income_cat"]):
    strat_train_set  = housing.loc[train_index].drop("income_cat", axis=1)
    strat_test_set  = housing.loc[test_index].drop("income_cat", axis=1)



housing = strat_train_set.copy()

housing_labels = housing['median_house_value'].copy()
housing = housing.drop('median_house_value',  axis=1).copy()

num_attribs = housing.drop("ocean_proximity", axis=1).columns.tolist()
cat_attribs = ["ocean_proximity"]


num_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

cat_pipeline = Pipeline([
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

full_pipeline = ColumnTransformer([
    ("num", num_pipeline, num_attribs),
    ("cat", cat_pipeline, cat_attribs)
])

housing_prepared = full_pipeline.fit_transform(housing)


feature_names = full_pipeline.get_feature_names_out()

housing_prepared_df = pd.DataFrame(
    housing_prepared,
    columns=feature_names,
    index=housing.index
)
# print(housing_prepared_df)


