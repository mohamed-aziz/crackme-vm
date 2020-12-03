#include <stdint.h>
#include <iostream>

#define CODE_SEGMENT_SIZE  2048
#define MEM_SEGMENT_SIZE 512
// #define DEBUG

typedef struct VM
{
    int32_t pc;
    uint8_t REG1, REG2, REG3, REG4;
    uint8_t *program;
    uint8_t *preg[4];
    uint8_t *data_offset;
} VM;

using namespace std;

#define HALT 101


void emulate(VM* vm) {
    // 16 bit instructions
    // OPCODE ARG1 ARG2
    do {
        // opcode
        int32_t pc = vm->pc;
        uint8_t u = vm->program[pc];
        // arg1
        uint8_t t = vm->program[pc+1];
        // arg2
        uint8_t v = vm->program[pc+2];
        bool jumped = false;
        
        switch (u) {
            case 1:
            {
              // MUL REG cst
              uint8_t *reg = vm->preg[t];
              *reg *= v;
              #ifdef DEBUG
              cerr << "MUL REG" << t+1 << ", "<< +v << endl;
              #endif
              break;
            }
            case 2:
            {
              // SUB REG1 cst
              uint8_t *reg = vm->preg[t];
              *reg -= v;
              #ifdef DEBUG
              cerr << "SUB REG" << t+1 << ", "<< +v << endl;
              #endif
              break;
            }
            case 3:
            {
              // NOT REG1
              uint8_t *reg = vm->preg[t];
              *reg = ~(*reg);
              #ifdef DEBUG
              cerr << "NOT REG" << t+1 << endl;
              #endif

              break;
            }
            case 4:
            {
              // XOR REG1 mem
              uint8_t *reg = vm->preg[t];

              uint8_t *val = vm->data_offset + v;
              *reg ^= *val;

              #ifdef DEBUG
              cerr << "XOR REG" << t+1 << ", "<< +(*val)<< endl;
              #endif
              break;
            }

            case 5:
            {
              // MOVI REG1 REG2
              uint8_t *reg = vm->preg[t];
              uint8_t *reg2 = vm->preg[v];
              *reg = *reg2;
              #ifdef DEBUG
              cerr << "MOVI REG" << t+1 << ", REG"<< v+1 << endl;
              #endif

              break;
            }

            case 6:
            { 
              // MOV REG mem
              uint8_t *reg = vm->preg[t];
              uint8_t *val = vm->data_offset + v;
              *reg = *val;
              #ifdef DEBUG
              cerr << "MOV REG" << t+1 << ", "<< +(*val) << endl;
              #endif

              break;
            }

            case 7:{
              // JMP IF REG1 != 0
              if (vm->REG1) { 
                  uint8_t tr = t;
                  vm->pc = tr + vm->pc;
                  jumped = true;
              }
              #ifdef DEBUG
              cerr << "JMP if REG1 " << t << " else "<< v << endl;
              #endif
              break;
            }

            case 8: {
                // OUT, REG1
                putc(vm->REG1, stdout);
                break;
            }

            case 9: {
                // EXIT handler
                exit(vm->REG1);
                break;
            }

            case 10: {
                // IN
                vm->REG1 = getc(stdin);
                #ifdef DEBUG
                cerr << "IN REG1" << endl;
                #endif
                break;
            }

            case 11: {
                // LSHIFT REG cst
                uint8_t *reg = vm->preg[t];
                *reg <<= v;
                #ifdef DEBUG
                cerr << "LSHIFT REG" << t+1 << ", " << +v << endl;
                #endif
                break;
            }

            case 12: {
                // AND REG mem
                uint8_t *reg = vm->preg[t];
                uint8_t *val = vm->data_offset + v;
                *reg &= *val;
                #ifdef DEBUG
                cerr << "AND REG" << t+1 << ", "<< +(*val) << endl;
                #endif
                break;
            }

            case 13: {
                // OR REG mem
                uint8_t *reg = vm->preg[t];
                uint8_t *val = vm->data_offset + v;
                *reg |= *val;
                #ifdef DEBUG
                cerr << "OR REG" << t+1 << ", "<< +(*val) << endl;
                #endif
                break;
            }

            case 14: {
                // ADD REG REG 
                uint8_t *reg = vm->preg[t];
                uint8_t *reg2 = vm->preg[v];
                *reg += *reg2;
                #ifdef DEBUG
                cerr << "ADD REG" << t+1 << ", REG"<< v+1 << endl;
                #endif
                break;
            }
        }
        if (!jumped) {
            vm->pc += 3;
        }

        #ifdef DEBUG
        cerr << "REG1: " << +vm->REG1 << ", REG2: "<< +vm->REG2 << ", REG3: "<< +vm->REG3 << ", REG4: "<< +vm->REG4 << ", PC: " << +vm->pc<< endl;
        #endif

    } while (vm->program[vm->pc] != HALT);

    #ifdef DEBUG
    if (vm->program[vm->pc] == HALT) {
        cerr << "HALT" << endl;
    }
    #endif

}

void init_vm_object(VM* vm) {
    vm->REG1 = vm->REG2 = vm->REG3 = vm->REG4 = 0;
    vm->preg[0] = &vm->REG1;
    vm->preg[1] = &vm->REG2;
    vm->preg[2] = &vm->REG3;
    vm->preg[3] = &vm->REG4;
    vm->data_offset = vm->program + CODE_SEGMENT_SIZE;
}

int main(int argc, char **argv) {
    uint8_t program[] = PROGRAMHERE

    VM *vm = (VM*) malloc(sizeof(VM));
    vm->program = program;
    init_vm_object(vm);
    emulate(vm);
}