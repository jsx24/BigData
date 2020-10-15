package bigdata.kafka.consumer;

import java.nio.ByteBuffer;
import java.util.Arrays;
import java.util.Iterator;
import kafka.api.FetchRequest;
import kafka.api.FetchRequestBuilder;
import kafka.cluster.BrokerEndPoint;
import kafka.javaapi.FetchResponse;
import kafka.javaapi.PartitionMetadata;
import kafka.javaapi.TopicMetadata;
import kafka.javaapi.TopicMetadataRequest;
import kafka.javaapi.TopicMetadataResponse;
import kafka.javaapi.consumer.SimpleConsumer;
import kafka.javaapi.message.ByteBufferMessageSet;
import kafka.message.MessageAndOffset;

public class LowApiConsumer {
    public LowApiConsumer() {
    }

    public static void main(String[] args) throws Exception {
        BrokerEndPoint leader = null;
        String host = "linux1";
        int port = 9092;
        SimpleConsumer metaConsumer = new SimpleConsumer(host, port, 500, 10240, "metadata");
        TopicMetadataRequest request = new TopicMetadataRequest(Arrays.asList("first"));
        TopicMetadataResponse response = metaConsumer.send(request);
        Iterator var7 = response.topicsMetadata().iterator();

        label37:
        while(var7.hasNext()) {
            TopicMetadata topicMetadata = (TopicMetadata)var7.next();
            if ("first".equals(topicMetadata.topic())) {
                Iterator var9 = topicMetadata.partitionsMetadata().iterator();

                while(var9.hasNext()) {
                    PartitionMetadata partitionMetadata = (PartitionMetadata)var9.next();
                    int partid = partitionMetadata.partitionId();
                    if (partid == 1) {
                        leader = partitionMetadata.leader();
                        break label37;
                    }
                }
            }
        }

        if (leader == null) {
            System.out.println("Error");
        } else {
            SimpleConsumer consumer = new SimpleConsumer(leader.host(), leader.port(), 500, 10240, "accessLeader");
            FetchRequest req = (new FetchRequestBuilder()).addFetch("first", 1, 5L, 10240).build();
            FetchResponse resp = consumer.fetch(req);
            ByteBufferMessageSet messageSet = resp.messageSet("first", 1);
            Iterator var20 = messageSet.iterator();

            while(var20.hasNext()) {
                MessageAndOffset messageAndOffset = (MessageAndOffset)var20.next();
                ByteBuffer buffer = messageAndOffset.message().payload();
                byte[] bs = new byte[buffer.limit()];
                buffer.get(bs);
                String value = new String(bs, "UTF-8");
                System.out.println(value);
            }

        }
    }
}