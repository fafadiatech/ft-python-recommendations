from datasets.content import NewsDataset

def test_news_dataset_download():
    dataset = NewsDataset()
    assert dataset is not None

    dataset.download_and_unzip()
    dataset.download_post_process()
    assert dataset.total_instances() != 0
    assert dataset.total_instances() == 422418
