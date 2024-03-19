import petl as etl


def download_file(url, local):
  source=etl.io.remotes.RemoteSource(url)
  etl.fromcsv(source).tocsv(local)
