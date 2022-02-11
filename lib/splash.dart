import 'package:flutter/material.dart';

import 'home.dart';

class Splash extends StatefulWidget {
  const Splash({Key? key}) : super(key: key);

  @override
  State<Splash> createState() => _SplashState();
}

class _SplashState extends State<Splash> {
  @override
  void initState(){
    super.initState();
    _navigatetohome();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Container(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                height: MediaQuery.of(context).size.height *0.8,
                width: MediaQuery.of(context).size.width *0.8,
                decoration: const BoxDecoration(
                  image: DecorationImage(
                    image: ExactAssetImage(
                      'lib/assets/images/yearn.png'
                    ),
                    fit: BoxFit.fill
                  )
                ),
              )
            ],
          ),
        ),
      ),
    );
  }

  _navigatetohome()async
  {
    await Future.delayed(Duration(milliseconds: 3000),(){});
    Navigator.pushReplacement(context, MaterialPageRoute(builder: (context)=>yearnHome()));
  }
}
