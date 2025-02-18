#include <libp2p/swarm.h>  

void propagate_update(const MapDelta *delta) {  
    struct Swarm *swarm = swarm_new("/broadmap/1.0");  
    uint8_t *serialized;  
    size_t len = serialize_delta(delta, &serialized);  
    
    swarm_publish(swarm, "map_updates", serialized, len);  
    swarm_broadcast(swarm, NEARBY_PEERS);  
}  