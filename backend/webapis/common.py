import re
def cssFilter(content):
    content=re.sub(r'style=\"(.*?)\"','',content)
    content=re.sub(r'class=\"(.*?)\"','',content)
    content=re.sub(r'<script[^>]*>([\s\S](?!<script))*?</script>','',content)
    # content=re.sub(r'<script(.*?)script>','',content)
    return content

if __name__ == "__main__":
    t = cssFilter('style="asldkjasdjlaksjdlkaj: asdas;"')
    print(t)