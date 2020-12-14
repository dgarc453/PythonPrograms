
//Dayana?tud?es?CS
//Da?a
//DayanaStudiesCS
//?????????
//an??jkss;
//?ayana
//Dayan?
public class Solution {

    public void main() {

    }

    public String replace(String originalWord) {
        return "";
    }

    private char generateLetter(char ogLetter) {
        int base = 97;
        char temp = ' ';
        while (base <= 122) {
            temp = (char) base;
            if (temp != ogLetter) {
                return temp;
            }
            base++;
        }
        return ' ';
    }
}