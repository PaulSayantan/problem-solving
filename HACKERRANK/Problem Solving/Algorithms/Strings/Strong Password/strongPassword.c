/**
 * @file strongPassword.c
 * @author Sayantan Paul
 * @brief Strong Password
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int checkPassword(char*);

int main() {
    char* password = (char*)malloc(100*sizeof(char));

    printf("Enter your password: ");
    scanf("%[^\n]s", password);
    
    printf("Required: %d\n", checkPassword(password));
    
    return 0;
}

int checkPassword(char* pass) {
    bool lc_flag = false, d_flag = false, uc_flag = false, sc_flag = false; 
    int missing_count = 0;
    int pass_size = strlen(pass);
    
    if (pass_size < 6)
        missing_count = 6 - pass_size;
    
    for (int i = 0; *(pass + i); i++) {
        int ch = *(pass + i);
        if (ch >= 97 && ch <= 122 && !lc_flag) {
            printf("\n[Success]: one lowercase character present\n");
            lc_flag = true;
        }
        else if (ch >= 65 && ch <= 90 && !uc_flag) {
            printf("\n[Success]: one uppercase character present\n");
            uc_flag = true;
        }
        else if (ch >= 48 && ch <= 57 && !d_flag) {
            printf("\n[Success]: one digit character present\n");
            d_flag = true;
        }
        else if ((ch == 33 || ch == 64 || ch == 94 || (ch >= 35 && ch <= 38) || (ch >= 40 && ch <= 43) || ch == 45) && !sc_flag) {
            printf("\n[Success]: one special character present\n");
            sc_flag = true;
        }
    }
    int required_chars = 4 - ((int)lc_flag + (int)sc_flag + (int)uc_flag + (int)d_flag);
    printf("Number of missing characters: %d\n", missing_count);
    printf("Number of required characters: %d\n", required_chars);

    if (missing_count <= required_chars)
        return required_chars;
    else
        return missing_count;
}