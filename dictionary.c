// Implements a dictionary's functionality

#include <stdbool.h>
#include <string.h>
#include "dictionary.h"
#include <stdlib.h>
#include <ctype.h>
#include <stdio.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 1000;

// Hash table
node *table[N];

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int index = hash(word);
    node* cursor = table[index];
    while(cursor != NULL)
    {
        if(strcasecmp(cursor->word,word) == 0)
        {
            return true;
        }
        cursor=cursor->next;
    }
    
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int total=0;
    for(int i=0;i<strlen(word);i++)
    {
        total += tolower(word[i]);
    }
    
    return (total % N);
}
    int words_count = 0;
// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    
    FILE *file=fopen(dictionary,"r");
    if(file==NULL)
    {
        return false;
    }
    char letter[45 + 1];
    unsigned int index;
     while(fscanf(file,"%s",letter) != EOF)
    {
        words_count += 1;
        node* new_node = malloc(sizeof(node));
        if(new_node == NULL)
            return false;
            
        strcpy(new_node->word,letter);
        index = hash(letter);
        new_node->next = NULL;
        
        if(table[index] == NULL)
        {
            table[index] = new_node;
        }
        else
        {
            new_node->next = table[index];
            table[index] = new_node;
        }
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return words_count;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    int i;
    bool done=false;
    
    for(i = 0; i <= N;i++)
    {
        if(table[i] != NULL)
        {
            node* head = table[i];
            node* del = table[i];
            bool end_of_loop = false;
            
            while(end_of_loop != true)
            {
                head = head->next;
                free(del);
                del->next = NULL;
                del = head;
                if(head->next == NULL)
                {
                    
                    free(head);
                    head->next = NULL;
                    end_of_loop = true;
                }
            }
        }    
        if(i == N)
        {
            done = true;
        }
    }
    if(done==true)
        return true;   
    else
        return false;
}
