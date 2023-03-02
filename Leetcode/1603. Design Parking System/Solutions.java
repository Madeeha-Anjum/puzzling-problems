class Solutions {
    int big;
    int medium;
    int small;

    public Solutions(int big, int medium, int small) {
        this.big = big;
        this.medium = medium;
        this.small = small;
        System.out.println("Hello World");
    }

    public static void main(String[] args) {

        Solutions name = new Solutions(1, 1, 0);
        System.out.println(name.addCar(1));
        System.out.println(name.addCar(2));
        System.out.println(name.addCar(3));
        System.out.println(name.addCar(1));

    }

    /*
     * CarType: 1= big ; 2= medium; 3= small;
     */

    public Boolean addCar(int carType) {

        if (carType == 1) {
            if (this.big != 0) {
                this.big = this.big - 1;
                return true;
            } else {
                return false;
            }

        } else if (carType == 2) {
            if (this.medium != 0) {
                this.medium = this.medium - 1;
                return true;
            } else {
                return false;
            }

        } else if (carType == 3) {

            if (this.small != 0) {
                this.small = this.small - 1;
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    }

}
