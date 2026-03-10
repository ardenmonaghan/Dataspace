# rm -rf backend/datasets/*
from db_helpers.db_services import get_sample_rows
from db_helpers.db_metadata import list_datasets

# Test getting sample rows from the dataset
def test_get_sample_rows():
    # Example dataset id
    dataset_id = "17adf15f-c696-454b-8186-9a8d61b74038"
    # Retrieve the dataset from the database.
    dataset = get_dataset_by_id(dataset_id)

    # Get the sample rows from the dataset.
    sample_rows = get_sample_rows(dataset, 10, "test_table")
    print(sample_rows)

# Test getting sample rows from the dataset

# Test uploading a dataset to the DB and the metadata being saved correctly. 

# Test get all table names from the dataset

if __name__ == "__main__":
    test_get_sample_rows()