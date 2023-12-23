class Fruits {
	private String fruitName;
	private String fruitColor;

	def setFruitName(String name) {
		fruitName = name
	}
	def seFruitColor(String color) {
		fruitColor = color
	}

	def getFruitName() {
		println "Name of fruits  is $fruitName"
	}
	def getFruitColor() {
		println "Color of fruit is $fruitColor"
	}

	static void main(args) {
		Fruits apple = new Fruits()
		apple.setFruitName("apple")
		apple.seFruitColor("REd")

		apple.getFruitColor()
		apple.getFruitName();
	}

}
