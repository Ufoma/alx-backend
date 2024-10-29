#!/usr/bin/env python3
import csv
import math

def index_range(page, page_size):
  """
  Returns a tuple of start and end indexes for pagination

  Parameters:
  - page (int): The page number (1-indexed)
  - page_size (int): Number of items per page

  Returns:
  -tuple: start, end
  """
  start = (page - 1) * page_size
  end = start + page_size
  return (start, end)
