import 'package:flutter/material.dart';

class yearnHome extends StatefulWidget {
  const yearnHome({Key? key}) : super(key: key);

  @override
  _yearnHomeState createState() => _yearnHomeState();
}

class _yearnHomeState extends State<yearnHome> {
  @override
  var selectProduct;
  Widget build(BuildContext context) {
    final home = Scaffold(
      appBar: AppBar(
        title: Text('  Yearn'),
        centerTitle: true,
      ),
      body: Column(
        children: [
          Container(
              child: OutlinedButton.icon(
                  onPressed: () async {
                    selectProduct = await showSearch(
                        context: context,
                        delegate: SearchBar(
                            products: ["ipad", "iphone", "macbook"],
                            suggestions: ["iphone"]));
                  },
                  icon: const Icon(Icons.search),
                  label: const Text("search")),
              width: MediaQuery.of(context).size.width),
          Container(
            child: PromotionBanner()
          ),
        ],
      ),
      bottomNavigationBar: const NavBar(),
    );
    print(selectProduct);
    return home;
  }
}

class PromotionBanner extends InkWell{
  const PromotionBanner({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context)
  {
    return InkWell(
      child: Card(
          clipBehavior: Clip.antiAlias,
          shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(15)),
          child:
          Image(image:AssetImage('lib/assets/images/bannerPromocoesText.png'),
              fit: BoxFit.fill
          )
      ),
      onTap: ()=>{print("promotion banner clicked") },
    );
  }

}

class NavBar extends StatefulWidget {
  const NavBar({Key? key}) : super(key: key);

  @override
  _NavBarState createState() => _NavBarState();
}

class _NavBarState extends State<NavBar> {
  var _currentIndex = 1;
  @override
  Widget build(BuildContext context) {
    return BottomNavigationBar(
      currentIndex: _currentIndex,
      items: const [
        BottomNavigationBarItem(
            icon: Icon(Icons.file_copy),
            label: "articles",
            backgroundColor: Colors.blue),
        BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: "home",
            backgroundColor: Colors.blue),
        BottomNavigationBarItem(
            icon: Icon(Icons.support_agent),
            label: "Sac",
            backgroundColor: Colors.blue),
        BottomNavigationBarItem(
            icon: Icon(Icons.person),
            label: "account",
            backgroundColor: Colors.blue),
      ],
      onTap: (index) {
        setState(() {
          _currentIndex = index;
        });
      },
    );
  }
}

class SearchBar extends SearchDelegate<String> {
  final List<String> products;
  final List<String> suggestions;

  @override
  SearchBar({required this.products, required this.suggestions});

  @override
  List<Widget>? buildActions(BuildContext context) {
    return [
      IconButton(
          onPressed: () {
            query = "";
          },
          icon: Icon(Icons.clear))
    ];
  }

  @override
  Widget? buildLeading(BuildContext context) {
    return IconButton(
        onPressed: () {
          query = '';
          close(context, query);
        },
        icon: Icon(Icons.arrow_back));
  }

  @override
  Widget buildResults(BuildContext context) {
    final List<String> allProducts = products
        .where((element) => element.toLowerCase().contains(query.toLowerCase()))
        .toList();

    return ListView.builder(
      itemBuilder: (context, index) => ListTile(
          title: Text(allProducts[index]),
          onTap: () {
            query = allProducts[index];
            close(context, query);
          }),
      itemCount: allProducts.length,
    );
  }

  @override
  Widget buildSuggestions(BuildContext context) {
    final List<String> productSuggestions = suggestions
        .where((element) => element.toLowerCase().contains(query.toLowerCase()))
        .toList();

    return ListView.builder(
      itemBuilder: (context, index) => ListTile(
        title: Text(products[index]),
        onTap: () {
          query = productSuggestions[index];
          close(context, query);
        },
      ),
      itemCount: productSuggestions.length,
    );
  }
}
