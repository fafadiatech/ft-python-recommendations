from datasets.content import NewsDataset

def test_news_dataset_download():
    dataset = NewsDataset()
    assert dataset is not None

    dataset.download_and_unzip()
    assert dataset.total_instances() != 0
