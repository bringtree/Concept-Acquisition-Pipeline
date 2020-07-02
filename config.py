class Evaluation:
    seed_filename = 'annotated-as-seed.json'
    evaluated_filenames = [
        'processed_concept_baidu/extraction_result/average_distance_result.json',
        'processed_concept_baidu/extraction_result/graph_prop_result.json',
        'processed_concept_baidu/extraction_result/pagerank_result.json',
        'processed_concept_baidu/extraction_result/tf_idf_result.json',
        'processed_concept_baidu/xlink_result/parsed_concept_baidu_1',
        'processed_concept_baidu/cluster_results/cluster_result.json',
        'processed_concept_baidu/rerank_results/rerank_result.json'
    ]
    algorithm_names = [
            'average_distance',
            'graph_prop',
            'pagerank',
            'tf_idf',
            'xlink',
            'cluster',
            'rerank']
    relevance_field_names = ['', '', '', '', 'freq', 'score', 'score']
    topks = [100, 200]
    dump_csv = 'evaluation_results.csv'
    file2algo = dict(zip(evaluated_filenames, algorithm_names))