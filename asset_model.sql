SELECT 
    a.ElementPath,a.TimeZone,a.Latitude,a.Longitude, mt.PIAFAttributeName,am.NumericValue, am.TextValue
FROM 
    def.Asset a
    INNER JOIN def.AssetTemplate [at] on a.[AssetTemplateID]=[at].[AssetTemplateID]
    INNER JOIN def.AssetMetadata [am] on a.AssetID=am.AssetID
    INNER JOIN def.MetadataTag [mt] on mt.MetadataTagID=am.MetadataTagID
WHERE 
    (a.AssetTemplateID=4 OR a.AssetTemplateID=3105)
    AND mt.PIAFAttributeName in ('MOUNTING_AZIMUTH','MOUNTING_GCR','MOUNTING_TILT', 'LOCATION_STATE', 'AC_CAPACITY')
    AND a.IsDeleted = 