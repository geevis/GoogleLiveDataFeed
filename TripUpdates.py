from google.transit import gtfs_realtime_pb2
import urllib

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen('http://192.237.29.212:8080/gtfsrealtime/TripUpdates')
feed.ParseFromString(response.read())
for entity in feed.entity:
  if entity.HasField('trip_update'):
    print entity.alert
    #print entity.vehicle;
    #print entity.trip_update;
    
  if entity.HasField('vehicle'):
    print entity.trip_update;print entity.vehicle;

print 'end'

    
