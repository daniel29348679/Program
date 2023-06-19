`timescale 1ns / 10ps
module simple_tb;
    reg a, b;

    initial begin
        //$dumpfile("simple.vcd");
        //$dumpvars(0, s);
        a <= 0;
        b <= 0;
        #10;
        a <= 1;
        b <= 1;
        #50 $finish;
    end

    always @(posedge a) begin
        if (b) $display("true");
        else $display("false");
    end

endmodule
