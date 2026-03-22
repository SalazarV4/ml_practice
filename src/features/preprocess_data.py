import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder

def get_preprocessor() -> ColumnTransformer:
    categorical_cols = ['checking_status',
                        'credit_history',
                        'purpose',
                        'savings_status',
                        'employment',
                        'personal_status',
                        'other_parties',
                        'property_magnitude',
                        'other_payment_plans',
                        'housing',
                        'job',
                        'own_telephone',
                        'foreign_worker']

    numeric_cols = ['duration',
                    'credit_amount',
                    'installment_commitment',
                    'residence_since',
                    'age',
                    'existing_credits',
                    'num_dependents']

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(sparse_output=False, handle_unknown='ignore'), categorical_cols),
            ("num", StandardScaler(), numeric_cols)
        ],
        verbose=True
    )

    return preprocessor

def get_train_test_data(preprocessor: ColumnTransformer,
                        df: pd.DataFrame,
                        label_col: str) -> None:
    X = df.drop(columns=[label_col], axis=1)
    y = df[label_col]

    encoder = LabelEncoder()
    y_enc = encoder.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y_enc,
                                                        test_size=0.2,
                                                        random_state=42,
                                                        stratify=y_enc)

    X_train = preprocessor.fit_transform(X_train)
    X_test = preprocessor.transform(X_test)

    return X_train, X_test, y_train, y_test
