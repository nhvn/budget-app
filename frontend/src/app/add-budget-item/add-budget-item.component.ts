import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-add-budget-item',
  templateUrl: './add-budget-item.component.html',
  styleUrls: ['./add-budget-item.component.css']
})
export class AddBudgetItemComponent implements OnInit {
  itemTitle: string = '';
  itemCost: number = 0;

  constructor() { }

  ngOnInit() {
  }

  addItem() {
    if (this.itemTitle && this.itemCost) {
      console.log("Item: " + this.itemTitle + ", Cost: " + this.itemCost);
    } else {
      console.error("Item title and cost are required");
    }
  }
}
