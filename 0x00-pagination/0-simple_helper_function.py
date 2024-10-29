#!/usr/bin/env python3

def index_range(page, page_size):
  """
  Returns a tuple of start and end indexes for pagination

  Parameters:
  - page (int): The page number (1-indexed)
  - page_size (int): Number of items per page

  Returns:
  -tuple: (start_index, end_index)
  """
  start_index = (page - 1) * page_size
  end_index = start_index + page_size
  return start_index, end_index
  
