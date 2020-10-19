package flume.interceptor;

import org.apache.flume.Context;
import org.apache.flume.Event;
import org.apache.flume.interceptor.Interceptor;

import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class LogTypeInterceptor implements Interceptor {

    @Override
    public void initialize() {

    }

    @Override
    public Event intercept(Event event) {

        // put the data type in body to header 

        // 1 get body data
        byte[] body = event.getBody();
        String log = new String(body, Charset.forName("UTF-8"));

        // 2 get header
        Map<String, String> headers = event.getHeaders();

        // 3 test
        if (log.contains("start")){
            headers.put("topic","topic_start");
        }else {
            headers.put("topic","topic_event");
        }

        return event;
    }

    @Override
    public List<Event> intercept(List<Event> events) {

        ArrayList<Event> interceptors = new ArrayList<>();

        for (Event event : events) {
            Event intercept = intercept(event);

            interceptors.add(intercept);
        }

        return interceptors;
    }

    @Override
    public void close() {

    }

    public static class  Builder implements Interceptor.Builder{

        @Override
        public Interceptor build() {
            return new LogTypeInterceptor();
        }

        @Override
        public void configure(Context context) {

        }
    }
}
