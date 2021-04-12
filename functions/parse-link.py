def handler(event, context):
    print(event)

    link_to_site = event['site']
    print(link_to_site)
    print(link_to_site.find('https://api.twitter.com'))
    link_type = 'RSS'
    print("TYPE RSS")

    if link_to_site.find('https://api.twitter.com') >= 0:
        print("TYPE Twitter")
        link_type = 'Twitter'
    return link_type
