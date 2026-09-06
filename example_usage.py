from client import ScientificConsensusRatioMapperClient

def main():
    client = ScientificConsensusRatioMapperClient()
    res = client.map_scientific_consensus()
    print('Scientific Consensus: ' + res['consensus_dossier_id'] + ' (' + res['consensus_grade'] + ')')
    print('Affirmative: ' + str(res['affirmative_ratio'] * 100) + '% | Sample Size: ' + str(res['combined_sample_size']))
    print('Dossier URL: ' + res['consensus_breakdown_url'])

if __name__ == '__main__':
    main()
