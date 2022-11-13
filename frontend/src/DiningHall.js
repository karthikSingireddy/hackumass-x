import React from 'react'
import berk from './berk';
import './diningHall.css'
import frank from './frank';
import hamp from './hamp';
import woo from './woo';
import Time from 'react-time';
class DiningHall extends React.Component {
    constructor(props) {
        super(props);
        console.log(props);
        this.props = props;
        this.canvas = React.createRef();
        // const context = this.canvas.current.getContext('2d');    
        // context.translate(0.5, 0.5);
        this.state = { t: 0 };
    }

    loadData() {
        const t = this;
        fetch(`http://localhost:5000/${this.props.name}`)
            .then(d => d.json())
            .then(data => {
                t.refresh();
                data.tables.forEach(table => {
                    let elapsed = Date.now() - table.time;
                    console.log("table.time is " + table.time);
                    console.log("elapsed is: " + elapsed);
                    let sec = Math.ceil((elapsed / 1000)) % 60;
                    let min = Math.ceil((elapsed) / (1000 * 60));
                    //console.log(Date.now());
                    t.drawTable(table.x, table.y, table.width, table.height, table.taken, min + ":" + sec);
                })
            });
    }

    componentDidMount() {
        this.componentDidUpdate(null, null);
        //get DPI
        let dpi = window.devicePixelRatio;
        //get context
        let ctx = this.canvas.current.getContext('2d');
        const originalHeight = this.canvas.current.height;
        const originalWidth = this.canvas.current.width;
        console.log("original height is " + originalHeight);
        //get CSS height
        //the + prefix casts it to an integer
        //the slice method gets rid of "px"
        let style_height = +getComputedStyle(this.canvas.current).getPropertyValue("height").slice(0, -2);
        //get CSS width
        let style_width = +getComputedStyle(this.canvas.current).getPropertyValue("width").slice(0, -2);
        //scale the canvas
        this.canvas.current.setAttribute('height', style_height * dpi);
        this.canvas.current.setAttribute('width', style_width * dpi);
        console.log("new height: " + this.canvas.current.height);
        let ratio = Math.max(
            originalWidth/style_width * dpi,
            originalHeight/style_height * dpi
        );
        console.log("ratio is " + ratio);
        ctx.scale(8, 8);
        ctx.translate(35, 0);
        this.interval = setInterval(() => this.setState({ t: Date.now()}), 1000);
    }

    componentWillUnmount() {
        clearInterval(this.interval);
    }

    componentDidUpdate(p, c) {
        console.log(p, c);
        this.loadData();
    }

    refresh() {
        const ctx = this.canvas.current.getContext('2d');
        ctx.clearRect(0, 0, this.canvas.current.width, this.canvas.current.height);
        switch(this.props.name) {
            case 'worcester':
                woo.draw(ctx, this.canvas);
                break;
            case 'frank':
                frank.draw(ctx, this.canvas.current);
                break;
            case 'hamp':
                hamp.draw(ctx, this.canvas.current);
                break;
            case 'berk':
                berk.draw(ctx, this.canvas.current);
                break;
            default:
                break
        }
    }

    drawTable(x, y, width, height, taken, time) {
        console.log('draw table')
        const canvas = this.canvas.current;
        const ctx = canvas.getContext('2d');
        const color = taken ? '#FF0000' : '#00FF00';

        ctx.fillStyle = color;
        ctx.fillRect(x, y, width, height);
        if (taken) {
            ctx.fillStyle = '#000000';
            ctx.font = "4px courier new";
            ctx.moveTo(x, y);
            ctx.fillText(time.toString(), x+1.9, y+8.35);
        }
    }

    render() {
        console.log(this.props.name);
        return <div className='mapContainer'>
            <canvas ref={this.canvas}/>
        </div>
    }
}

export default DiningHall;