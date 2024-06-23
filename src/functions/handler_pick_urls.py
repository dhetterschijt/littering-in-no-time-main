def create_url(gdf):

    base_url = "https://openlittermap.com/tags?custom_tag=certificate-76&lat={lat}&lon={lon}&zoom=30"

    def generate_url(row):
        return base_url.format(lat=row['lat'], lon=row['lon'])
    
    gdf['url'] = gdf.apply(generate_url, axis=1)

    return gdf


