<template>
    <div class= "question-box-container">
        <b-jumbotron>

         <template v-slot:lead>
           {{currentQuestion.question}}
         </template>
            <hr class="my-4">

            <b-list-group>
                <b-list-group-item  
                v-for ="answer in answers" :key="answer"
                @click.prevent="selectAnswer(answer)"
                :class = "{selected : selectedAnswer === answer}"
                >
                    {{answer}}                
                </b-list-group-item>

            </b-list-group>

             <p>
             </p>

            <b-button variant="primary" href="#">Submit</b-button>
            <b-button @click= "next" variant="success" href="#">Next</b-button>
        </b-jumbotron>
    </div>  
</template>

<script>
import _ from "lodash"
export default {
    props: {
        currentQuestion: Object,
        next: Function
    },
    data() {
        return {
            selectedAnswer : null,
            shuffledAnswers: []
        }
    }, 
    computed: {
        answers() {
            let answers = [...this.currentQuestion.incorrect_answers]
            answers.push(this.currentQuestion.correct_answer)
            return answers
        }
    },
    watch: {
       currentQuestion: {
           immediate: true,
           handler() {
               this.selectedAnswer = null
               this.shuffleAnswers()
           }
       }
    },
    methods: {
        selectAnswer(answer) {
            this.selectedAnswer = answer
        },
        shuffleAnswers() {
            let answers = [...this.currentQuestion.incorrect_answers, this.currentQuestion.correct_answer]
            this.shuffledAnswers = _.shuffle(answers)
        }
    }
    
}
</script>

<style scoped>
.btn {
    margin: 0 5px;
}
.list-group-item:hover {
    background: gray;
    cursor: pointer;
}
.selected {
    background-color: lightblue;
}
.correct {
    background-color: lightgreen;
}
.incorrect {
    background-color: lightcoral;
}
</style>