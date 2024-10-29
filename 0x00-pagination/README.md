# Pagination Project

## Project Overview
This project shows how to implement pagination in a dataset in Python using various techniques. The objective is to divide big datasets into digestible "pages" and enable smooth page navigation, even in the event that dataset items are removed.

## Features
1. **Simple Pagination** - Paginate a dataset using `page` and `page_size` parameters.
2. **Hypermedia Metadata** - Add extra information about the pagination state, such as total pages, current page, and next/previous pages.
3. **Deletion-Resilient Pagination** - Handle pagination in a way that doesn’t break if items are deleted.

## Learning Objectives
- Understand the basics of pagination and data slicing.
- Implement pagination with parameters for page number and page size.
- Add metadata to help with navigation.
- Make pagination resilient to deletions.

## Requirements
- Python 3.x

## Data used
[Popular baby names.csv](https://intranet.alxswe.com/rltoken/NBLY6mdKDBR9zWvNADwjjg)

## Setup
Clone this repository to your local machine and navigate to the project directory.

```bash
git clone <repository_url>
cd pagination_project
```

## How to Use
1. **Basic Pagination**:
   - Open `pagination.py` and find the `get_page` function.
   - Use this function to paginate a dataset by specifying the `page` and `page_size`.

2. **Pagination with Metadata**:
   - Check out the `get_page_with_metadata` function.
   - This function provides additional information such as `total_pages`, `next_page`, and `prev_page`.

3. **Deletion-Resilient Pagination**:
   - Use the `deletion_resilient_pagination` function (if implemented) to handle cases where items might be deleted.

## Example Usage
Below is an example of how to use the basic pagination function:

```python
# Sample dataset
data = [i for i in range(1, 101)]  # A list of numbers 1 to 100

# Import pagination functions
from pagination import get_page

# Retrieve items on page 2 with pag e size of 10
page_data = get_page(data, page=2, page_size=10)
print("Page 2 Data:", page_data)
```

## Project Structure
- `pagination.py`: Contains the functions for basic pagination, pagination with metadata, and deletion-resilient pagination.

## Additional Notes
- Test with different datasets and parameters to see how the pagination adapts.
