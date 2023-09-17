def search_for_pose(vector, shifty_collection):
    search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
    results = shifty_collection.search(
        data=[vector],
        anns_field="vector",
        top_k=1,
        param=search_params,
        limit=1,
        output_fields=['image_name'])
    similar_image_name = results[0][0].entity.get('image_name')
    return similar_image_name

