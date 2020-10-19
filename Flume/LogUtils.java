package flume.interceptor;

import org.apache.commons.lang.math.NumberUtils;

public class LogUtils {

    public static boolean validateStart(String log) {

        if (log == null){
            return false;
        }

        // json { }
        if (!log.trim().startsWith("{") || !log.trim().endsWith("}")){
            return false;
        }

        return true;
    }

    public static boolean validateEvent(String log) {
        // server time | json
        // 1549696569054 | {"cm":{"ln":"-89.2","sv":"V2.0.4","os":"8.2.0","g":"M67B4QYU@gmail.com","nw":"4G","l":"en","vc":"18","hw":"1080*1920","ar":"MX","uid":"u8678","t":"1549679122062","la":"-27.4","md":"sumsung-12","vn":"1.1.3","ba":"Sumsung","sr":"Y"},"ap":"weather","et":[]}

        if (log == null){
            return false;
        }

        // split
        String[] logContents = log.split("\\|");

        // test length of logContents
        if (logContents.length != 2){
            return false;
        }

        // test server time
        if (logContents[0].length()!=13 || !NumberUtils.isDigits(logContents[0])){
            return false;
        }

        // test json
        // json { }
        if (!logContents[1].trim().startsWith("{") || !logContents[1].trim().endsWith("}")){
            return false;
        }

        return true;
    }
}
