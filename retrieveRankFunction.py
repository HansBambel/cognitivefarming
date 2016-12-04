import json
from watson_developer_cloud import RetrieveAndRankV1
import re


def retrieveRankFunction(inp):
    # 4 spaces
    retrieve_and_rank = RetrieveAndRankV1(username='7dcf9b9a-a6e1-4ca7-bbeb-4cfbebf0f52c', password='jGdGbHVpXAq6')

    # checking out our clusters
    solr_clusters = retrieve_and_rank.list_solr_clusters()
    #print(json.dumps(solr_clusters, indent=2))

    # Replace with your own solr_cluster_id
    solr_cluster_id = 'sce8bd4302_0e95_4499_9dbf_f97d52b0cba4'

    #changing to our cluster
    #status = retrieve_and_rank.get_solr_cluster_status(solr_cluster_id=solr_cluster_id)
    #print(json.dumps(status, indent=2))

    configs = retrieve_and_rank.list_configs(solr_cluster_id=solr_cluster_id)
    #print(json.dumps(configs, indent=2))

    if len(configs['solr_configs']) > 0:
        collections = retrieve_and_rank.list_collections(solr_cluster_id=solr_cluster_id)
        pysolr_client = retrieve_and_rank.get_pysolr_client(solr_cluster_id, collections['collections'][0])

        #search_for = input("Was soll ich übersetzen?: ")
        search_for = inp
        if search_for == 'NG312' or search_for == 'SE1201'or search_for == 'SF6142'or search_for == 'NN400'or search_for == 'NW811':
            info = 'Keine Information vorhanden. '
        else:
            results = pysolr_client.search(search_for)
            resultingString = str(results.docs)
            description = re.search('</td><td><p dir="ltr">(.+?)</p></td></tr> <tr><td>',resultingString)
            info = description.group(1)
            info2 = re.sub('<.*?>', '', info)
            #print(description.group(1))
        #print(info)
        return(info2)

    return 


strr = retrieveRankFunction('NT699')
print(strr)
