// const cypress = require("cypress")

describe('Youtube Search Testing', () => {
    it('Does not do much!', () => {
      cy.visit("https://www.alsacreations.com/quiz/");

      cy.get(':nth-child(1) > .quiz-title > .h-link').click();

      
      cy.contains("Quiz HTML débutant").should('be.visible');

      cy.get('#q0r2').click();
      cy.get('#q1r2').click();
      cy.get('#q2r4').click();
      cy.get('#q3r1').click();
      cy.get('#q4r6').click();
      cy.get('#q5r1').click();
      cy.get('#q6r5').click();
      cy.get('#q7r3').click();
      cy.get('#q8r2').click();
      cy.get('#q9r1').click();


      cy.get('.center > .awesome').click();

      cy.get('.quiz-score-value').invoke("text").should("eq", "10/10");
    })
  })