"""
benchmark_time_required is a tool that is used to generate timing
information for different algorithms
"""
import os
import sys
import logging
import functools
from timeit import Timer
from pathlib import Path

sys.path.append(os.path.join(Path(__file__).parent.parent,))

from datasets.content import NewsDataset
from models.content import CountBased

logging.basicConfig(filename="time_required.log", level=logging.INFO)

def benchmark_training_time(recommender, dataset, recommender_name, dataset_name):
    """
    time_algorithm is used to time different algorithms
    """
    start_log = f"Benchmarking {recommender_name} algorithm using {dataset_name}"
    logging.info(start_log)
    recommender.train(dataset.get_instances())

if __name__ == "__main__":
    dataset = NewsDataset(200)
    recommender = CountBased()
    timer = Timer(functools.partial(
        benchmark_training_time, recommender, dataset,
        "Count Based", "BBC News Dataset"))
    execution_time = timer.timeit(1)
    timing_log = f"Execution took {execution_time}"
    logging.info(timing_log)
