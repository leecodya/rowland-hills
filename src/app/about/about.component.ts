import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';

@Component({
    selector: 'app-about',
    templateUrl: './about.component.html',
    styleUrls: ['./about.component.css']
})
export class AboutComponent implements OnInit {

    title = "Rowland Hills"

    constructor(private titleService: Title) {
        this.titleService.setTitle(`About Us | ${this.title}`);
    }

    ngOnInit(): void {
    }

}
