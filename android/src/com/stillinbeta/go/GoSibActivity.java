package com.stillinbeta.go;

import android.content.Context;
import android.net.http.AndroidHttpClient;
import android.view.View;
import android.view.View.OnClickListener;
import android.app.Activity;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.Button;
import android.content.pm.PackageManager;
import android.content.pm.PackageInfo;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.HttpResponse;
import org.apache.http.StatusLine;
import org.apache.http.impl.client.DefaultHttpClient;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import android.content.pm.PackageManager.NameNotFoundException;
import android.content.res.Resources;
import org.apache.http.entity.StringEntity;
import org.apache.http.util.EntityUtils;


public class GoSibActivity extends Activity
{
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        Button shorten = (Button)findViewById(R.id.shorten);
        shorten.setOnClickListener(sendUrl);

    }
    private String getVersion() {
        try {
            Context context = getApplicationContext();
            PackageManager pm = context.getPackageManager();
            PackageInfo info = pm.getPackageInfo(context.getPackageName(), 0);
            
            return info.versionName;
       } catch (NameNotFoundException e) {
           return "???";
       }
    }

    private OnClickListener sendUrl = new OnClickListener() {
        public void onClick(View v) {
            EditText url = (EditText)findViewById(R.id.url);
            Resources res = getResources();

            Context context = getApplicationContext();
            HttpPost post = new HttpPost(res.getString(R.string.api_url));
            try {
                StringEntity ent = new StringEntity("url=" + url.getText());
                post.setEntity(ent);
            } catch (UnsupportedEncodingException e) {}

            DefaultHttpClient client = new DefaultHttpClient();
            try {
                HttpResponse response = client.execute(post);
                StatusLine status = response.getStatusLine();
                String code = Integer.toString(status.getStatusCode());
                String word = EntityUtils.toString(response.getEntity());

                setContentView(R.layout.showurl);
                TextView shorten = (TextView)findViewById(R.id.noun);
                shorten.setText(word); 


            }
            catch (IOException  e) {
                Toast.makeText(context, e.toString(), Toast.LENGTH_SHORT).show();
            }
        }
    };
}
