set -eu

webroot="/usr/share/nginx/html/csd.uoc.gr"

cd $webroot

if [ ! -s "${webroot}/index.html" ]; then
  echo "downloading csd..."
  wget --no-check-certificate -E -k -p "https://csd.uoc.gr"
else
  echo "content already exists"
fi

if [ ! -s "${webroot}/index.html" ]; then
  echo "error: download failed"
  exit 1
fi
