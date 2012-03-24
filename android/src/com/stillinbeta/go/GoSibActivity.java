package com.stillinbeta.go;

import android.content.Context;
import android.view.View;
import android.view.View.OnClickListener;
import android.app.Activity;
import android.os.Bundle;
import android.widget.Toast;
import android.widget.Button;

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

    private OnClickListener sendUrl = new OnClickListener() {
        public void onClick(View v) {
            Context context = getApplicationContext();
            Toast toast = Toast.makeText(context, "OHAI!", Toast.LENGTH_SHORT);
            toast.show();
        }
    };
}
